import os
import pathlib
import platform
import subprocess
import time
import unittest

from .utils import check_pkg_exists


class TestSlurm(unittest.TestCase):
    def test_sbatch(self):
        # Checks for successful installation of sbatch
        self.assertTrue(check_pkg_exists('sbatch'))

    def test_srun(self):
        # Checks for successful installation of srun
        self.assertTrue(check_pkg_exists('srun'))

    def test_squeue(self):
        # Checks for successful installation of squeue
        self.assertTrue(check_pkg_exists('squeue'))

    def test_sinfo(self):
        # Checks for successful installation of sinfo
        self.assertTrue(check_pkg_exists('sinfo'))

    def test_scontrol(self):
        # Checks for successful installation of scontrol
        self.assertTrue(check_pkg_exists('scontrol'))

    def test_run_srun(self):
        # Checks that running a job with `srun` results in
        # expected output
        output = subprocess.run(['srun', 'hostname'], stdout=subprocess.PIPE)
        self.assertEqual(output.stdout.decode('UTF-8').strip(), platform.node())

        output = subprocess.run(['srun', 'pwd'], stdout=subprocess.PIPE)
        self.assertEqual(output.stdout.decode('UTF-8').strip(), os.getcwd())

    def test_run_sbatch(self):
        # Checks that running a job with `sbatch` results in
        # expected output
        run_dir = pathlib.Path(
                      os.environ.get('RUNNER_TEMP', '~')
                  ).expanduser().resolve()
        os.chdir(run_dir)

        # Create job submission script
        with open('run.sh', 'w', encoding='UTF-8') as fileID:
            fileID.write(
                '#!/bin/bash\n\n'
                'echo Docker containers are awesome\n'
                'pwd\n'
                'hostname\n'
                'echo $SLURM_JOBID\n'
                'echo $SLURM_JOB_ACCOUNT\n'
                'echo $SLURM_JOB_NUM_NODES\n'
                'echo $SLURM_TASKS_PER_NODE\n'
            )

        # Run job
        job_log = run_dir / 'job_log.txt'
        self.assertFalse(job_log.exists())

        output = subprocess.run(
            ['sbatch', '--account=debug', '--nodes=1', '--ntasks-per-node=1',
             '--cpus-per-task=1', f'--output={job_log}', 'run.sh'],
            stdout=subprocess.PIPE
        )
        stdout = output.stdout.decode('UTF-8').strip().split()

        # Check that output matches expected format
        self.assertEqual(len(stdout), 4)
        self.assertEqual(' '.join(stdout[0:3]), 'Submitted batch job')
        job_id = stdout[-1]     # Get Job ID

        # Wait for jobs to finish running, up to 120 seconds
        t0 = time.time()
        while (time.time() - t0 <= 120):
            # Get Job IDs of running jobs
            output = subprocess.run(['squeue', '-h', '--format=%A'],
                                    stdout=subprocess.PIPE)

            # If no jobs are running, exit loop
            if len(output.stdout.decode('UTF-8').split()) == 0:
                break

        # Check that job output log matches expected format
        self.assertTrue(job_log.is_file())

        with open(job_log, 'r', encoding='UTF-8') as fileID:
            job_log_contents = fileID.read()

        self.assertEqual(
            job_log_contents,
            (
                f'Docker containers are awesome\n'
                f'{run_dir}\n'
                f'{platform.node()}\n'
                f'{job_id}\n'
                f'debug\n'
                f'1\n'
                f'1\n'
            )
        )

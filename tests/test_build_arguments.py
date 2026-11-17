"""Verify CMake arguments using shell functions instead of executing builds."""

from __future__ import annotations

import os
import subprocess
import textwrap
import unittest
from pathlib import Path


class BuildArgumentsTests(unittest.TestCase):
    """Verify targets cannot inject build-system options through word splitting."""

    def test_target_is_one_argument_and_jobs_are_numeric(self) -> None:
        """Exercise the shipped argument code without the container entrypoint."""
        action = (Path(__file__).parents[1] / "action.yaml").read_text()
        script = textwrap.dedent(action.split('        jobs="', 1)[1].split("      env:", 1)[0])
        script = 'jobs="' + script
        helpers = 'nproc() { printf "2\\n"; }; cmake() { printf "<%s>\\n" "$@"; };\n'
        for target, jobs, succeeds in [
            ("named target", "2", True),
            ("-- --tool", "2", False),
            ("x", "2 --bad", False),
            ("x\n::error::forged", "2", False),
        ]:
            with self.subTest(target=target):
                result = subprocess.run(
                    ["bash", "-e", "-c", helpers + script],
                    capture_output=True,
                    text=True,
                    env={"PATH": os.environ["PATH"], "TARGET": target, "PARALLEL_JOBS": jobs},
                )
                self.assertEqual(result.returncode == 0, succeeds, result.stderr)
                if succeeds:
                    self.assertIn("<named target>", result.stdout)


if __name__ == "__main__":
    unittest.main()

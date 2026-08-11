import json
import os
import platform
import shutil
import subprocess
import sys
from config import settings

class AllureHelper:
    
    @staticmethod
    def create_environment(results_dir):
        """Create environment metadata for Allure report"""
        
        os.makedirs(results_dir, exist_ok=True)

        environment = {
            "Project": "Demoqa Bookstore API",
            "Environment": settings.ENVIRONMENT,
            "OS": platform.platform(),
            "Python": sys.version.split()[0],
        }

        with open(
            os.path.join(results_dir, "environment.properties"),
            "w",
            encoding="utf-8",
        ) as file:
            for key, value in environment.items():
                file.write(f"{key}={value}\n")

    @staticmethod
    def create_executor(results_dir):
        """Create executor metadata for local and CI execution"""
        
        os.makedirs(results_dir, exist_ok=True)

        if os.getenv("CI", "").lower() == "true":
            executor = {
                "name": "CI - GitHub Actions",
                "type": "github",
                "buildName": os.getenv("GITHUB_WORKFLOW", "API Automation Pipeline"),
                "buildOrder": os.getenv("GITHUB_RUN_NUMBER", 1),
                "buildUrl": (
                    f"{os.getenv('GITHUB_SERVER_URL', '')}/"
                    f"{os.getenv('GITHUB_REPOSITORY', '')}/actions/runs/"
                    f"{os.getenv('GITHUB_RUN_ID', '')}"
                ),
                "reportName": "Bookstore API Automation Test Report",
            }
        else:
            executor = {
                "name": "Local - Maolana Hadiar",
                "type": "local",
                "buildName": "Manual Execution",
                "buildOrder": 1,
                "reportName": "Bookstore API Automation Test Report",
            }

        with open(
            os.path.join(results_dir, "executor.json"),
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(executor, file, indent=4)

    @staticmethod
    def copy_history(results_dir, report_dir):
        """Copy previous Allure history to keep trend information"""
        
        source = os.path.join(report_dir, "history")
        destination = os.path.join(results_dir, "history")

        if os.path.exists(source):
            shutil.copytree(
                source,
                destination,
                dirs_exist_ok=True,
            )

    @staticmethod
    def generate_report(results_dir, report_dir):
        """Generate Allure report from test results"""
        
        subprocess.run(
            [
                "allure",
                "generate",
                results_dir,
                "-o",
                report_dir,
                "--clean",
            ],
            check=True,
        )

    @staticmethod
    def open_report(report_dir):
        """Open Allure report in browser"""
        
        subprocess.run(
            [
                "allure",
                "open",
                report_dir,
            ],
            check=True,
        )
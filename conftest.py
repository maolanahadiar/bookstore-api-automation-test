from utils.allure_helper import AllureHelper
from config.settings import AUTO_OPEN_REPORT

RESULTS_DIR = "reports/allure-results"
REPORT_DIR = "reports/allure-report"

def pytest_sessionstart(session):
    """Prepare Allure metadata before test execution"""
    
    AllureHelper.create_environment(RESULTS_DIR)
    AllureHelper.create_executor(RESULTS_DIR)
    
def pytest_sessionfinish(session, exitstatus):
    """Generate and open Allure report based on config after test execution"""
    
    AllureHelper.copy_history(
        RESULTS_DIR,
        REPORT_DIR
    )

    if AUTO_OPEN_REPORT == True:
        AllureHelper.generate_report(
            RESULTS_DIR,
            REPORT_DIR
        )

        AllureHelper.open_report(REPORT_DIR)
        
pytest_plugins = [
    "fixtures.account_fixtures"
]
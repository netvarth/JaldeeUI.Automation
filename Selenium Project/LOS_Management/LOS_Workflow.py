from Framework.common_utils import *



@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Case: LOS work flow")
@pytest.mark.parametrize('url', ["https://scale.jaldee.com/business/"])
def test_los_workflow(login):

    try:
        wait = WebDriverWait(login, 10)




    except Exception as e:
        allure.attach(  # use Allure package, .attach() method, pass 3 params
            login.get_screenshot_as_png(),  # param1
            # login.screenshot()
            name="full_page",  # param2
            attachment_type=AttachmentType.PNG,
        )
        raise e
    

    
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class NewCompetitorTest(StaticLiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox(executable_path='/home/kruglov/anaconda3/envs/tubcheck_conda_django/bin/geckodriver')
        self.browser.implicitly_wait(2)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_competitor_can_register_and_answer(self):
        # main page opens up, inputbox is there
        self.browser.get(self.live_server_url)

        input_box = self.browser.find_element_by_id('id_input')

        # user enters test@test and hits Enter, first image appears
        input_box.send_keys('test@test\n')

        first_image = self.browser.find_element_by_id('image')
        first_image_src = first_image.get_attribute('src')

        self.assertEqual(first_image_src, 'MCUCXR_0055_0.png')

        # user chooses 'Tuber' option

        # user goes to next image

        # user chooses 'No tuber' option

        # user goes back to first image

        self.fail('Finish the functional test!')

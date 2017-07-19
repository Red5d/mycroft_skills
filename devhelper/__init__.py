from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from subprocess import call

class DevHelperSkill(MycroftSkill):
    def __init__(self):
        super(DevHelperSkill, self).__init__(name="DevHelperSkill")

    def initialize(self):
        self.__build_skillreload_intent()
        self.__build_reboot_intent()

    def __build_skillreload_intent(self):
        intent = IntentBuilder("ReloadIntent").require("DevHelperKeyword").require("Reload").build()
        self.register_intent(intent, self.handle_skillreload_intent)

    def __build_reboot_intent(self):
        intent = IntentBuilder("RebootIntent").require("DevHelperKeyword").require("Reboot").build()
        self.register_intent(intent, self.handle_reboot_intent)        

    def handle_skillreload_intent(self, message):
        # Requires a sudoers entry allowing user 'mycroft' to run this command
        self.speak("Reloading skills")
        call("sudo /bin/systemctl restart mycroft-skills", shell=True)

    def handle_reboot_intent(self, message):
        self.speak("Rebooting")
        call("sudo /sbin/reboot", shell=True)

    def stop(self):
        pass


def create_skill():
    return DevHelperSkill()

class PromptConstructor:
    def __init__(self):
        self.system_prompt = ""
        self.user_prompt = ""

    def set_system_prompt(self, system_prompt):
        self.system_prompt = system_prompt

    def set_user_prompt(self, user_prompt):
        self.user_prompt = user_prompt

    def construct_prompt(self):
        return f"Human: {self.system_prompt}\n\n{self.user_prompt}\n\nAssistant:"
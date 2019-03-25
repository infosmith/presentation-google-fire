import subprocess


class TestRad():

    script_tested = ('demo', 'rad.py')

    def test_greet_english(self, path_builder):
        script = path_builder(*self.script_tested)
        command = ' '.join(['python', script, 'greet', 'everyone'])
        expected_result = 'Hello everyone, welcome to Automate!\n'
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        assert result.stdout.decode('utf-8') == expected_result

    def test_greet_hindi(self, path_builder):
        script = path_builder(*self.script_tested)
        command = ' '.join(['python', script, 'greet', 'everyone', '--lang=hi'])
        expected_result = 'सभी को नमस्कार, स्वचालित में आपका स्वागत है!\n'
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        assert result.stdout.decode('utf-8') == expected_result

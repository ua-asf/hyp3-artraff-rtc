def test_hyp3_artraff_rtc(script_runner):
    ret = script_runner.run(['python', '-m', 'hyp3_artraff_rtc', '-h'])
    assert ret.success

from awesome import *
from mock import patch, Mock

def test_aw_fun():
	expected = 42
	acctual = awesome_fun()
	assert expected == acctual, "no good"

@patch('awesome.download_text_from_web')
def test_text_analysis(mock_call):
	mock_call.return_value = Mock()
	mock_call.return_value = "mock test"
	wc = do_text_analysis()
	assert wc > 0, "pass"

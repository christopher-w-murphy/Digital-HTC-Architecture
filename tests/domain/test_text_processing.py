from src.domain.text_processing import remove_excess_line_breaks


class TestRemoveExcessLineBreaks:
    def test_str(self):
        text = 'Earth-\nquake wrapped onto the next line.\n\nStart of next\nparagraph.\n\n'
        result = 'Earthquake wrapped onto the next line.\n\tStart of next paragraph.'
        assert remove_excess_line_breaks(text) == result

    def test_bytes(self):
        text = b'Earth-\nquake wrapped onto the next line.\n\nStart of next\nparagraph.\n\n'
        result = b'Earthquake wrapped onto the next line.\n\tStart of next paragraph.'
        assert remove_excess_line_breaks(text) == result

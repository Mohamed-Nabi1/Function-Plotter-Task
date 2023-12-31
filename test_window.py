import pytest
import main


@pytest.fixture
def app(qtbot):
    test_app = main.Window()
    qtbot.addWidget(test_app)
    return test_app


@pytest.fixture(scope='function', autouse=True)
def first_app(app, request):
    request.instance.app = app


class Test_general:

    # test that no error_message in normal case
    def test_no_error(self, request):
        assert request.instance.app.error_message.isHidden() == True

    # test plot button text
    def test_plot_text(self, request):
        assert request.instance.app.plot.text() == "Plot"

    # test plot button text
    def test_error_font(self, request):
        request.instance.app.function.setText("xy")
        request.instance.app.plot.click()
        assert (request.instance.app.error_message.font().family(),
                request.instance.app.error_message.font().pointSize()) == ("Times",12)


class Test_function:

    # test func_label text
    def test_func_label(self, request):
        assert request.instance.app.func_label.text() == "Function: "

    # test function starting text
    def test_function_text(self, request):
        assert request.instance.app.function.text() == "x"

    # test that function is an editable text box
    def test_editable(self, request):
        assert request.instance.app.function.isReadOnly() == False

    # test that function is an enabled text box
    def test_enabled(self, request):
        assert request.instance.app.function.isEnabled() == True

    # test that on_change signal is emitted when click 'plot'
    def test_onChange_signal(self, request, qtbot):
        with qtbot.waitSignal(request.instance.app.plot.clicked, timeout=10000):
            request.instance.app.plot.click()

    # test that error_message is shown if wrong word is written in function after clicking 'plot' e.g., xy
    def test_function_error(self, request):
        request.instance.app.function.setText("xy")
        request.instance.app.plot.click()
        assert request.instance.app.error_message.isHidden() == False


class Test_min_spinbox:

    # test min x starting value
    def test_value(self, request):
        assert request.instance.app.mn.value() == float(-1)

    # test minimum possible value
    def test_minimum_value(self, request):
        assert request.instance.app.mn.minimum() == float(-1000)

    # test maximum possible value
    def test_maximum_value(self, request):
        assert request.instance.app.mn.maximum() == float(1000)

    # test min x label
    def test_prefix(self, request):
        assert request.instance.app.mn_label.text() == "Minimum x: "

    # test that box is editable
    def test_editable(self, request):
        assert request.instance.app.mn.isReadOnly() == False

    # test that box is enabled
    def test_enabled(self, request):
        assert request.instance.app.mn.isEnabled() == True

    # test that decreasing value is allowed
    def test_stepdown(self, request):
        request.instance.app.mn.stepBy(-1)
        assert request.instance.app.mn.value() == float(-2)

    # test that increasing value is allowed 
    def test_stepup(self, request):
        request.instance.app.mn.stepBy(1)
        assert request.instance.app.mn.value() == float(0)

    # test that on-change signal is emitted when changing the value
    def test_onChange_signal(self, request, qtbot):
        with qtbot.waitSignal(request.instance.app.mn.valueChanged, timeout=10000):
            request.instance.app.mn.stepBy(5)

    # test that min x is less than max x otherwise error is shown
    def test_mn_limits(self, request):
        request.instance.app.mn.setValue(request.instance.app.mx.value())
        assert request.instance.app.error_message.isHidden() == False


class Test_max_spinbox:

    # test max x starting value
    def test_value(self, request):
        assert request.instance.app.mx.value() == float(1)

    # test minimum possible value
    def test_minimum_value(self, request):
        assert request.instance.app.mx.minimum() == float(-1000)

    # test maximum possible value
    def test_maximum_value(self, request):
        assert request.instance.app.mx.maximum() == float(1000)

    # test max x label
    def test_prefix(self, request):
        assert request.instance.app.mx_label.text() == "Maximum x: "

    # test that box is editable
    def test_editable(self, request):
        assert request.instance.app.mx.isReadOnly() == False

    # test that box is enabled
    def test_enabled(self, request):
        assert request.instance.app.mx.isEnabled() == True

    # test that decreasing value is allowed
    def test_stepdown(self, request):
        request.instance.app.mx.stepBy(-1)
        assert request.instance.app.mx.value() == float(0)

    # test that increasing value is allowed
    def test_stepup(self, request):
        request.instance.app.mx.stepBy(1)
        assert request.instance.app.mx.value() == float(2)

    # test that on-change signal is emitted when changing the value
    def test_onChange_signal(self, request, qtbot):
        with qtbot.waitSignal(request.instance.app.mx.valueChanged, timeout=10000):
            request.instance.app.mx.stepBy(5)

    # test that max x is greater than min x otherwise error is shown
    def test_mn_limits(self, request):
        request.instance.app.mx.setValue(request.instance.app.mn.value())
        assert request.instance.app.error_message.isHidden() == False

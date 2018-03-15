import pytest
import warnings

import matplotlib.pyplot as plt


@pytest.mark.backend('pdf')
def test_show_nongui_warning():
    plt.plot()

    with pytest.warns(UserWarning) as warns:
        plt.show()
        assert len(warns) == 1
        assert "matplotlib is currently using a non-GUI backend, " \
               "so cannot show the figure" == warns[0].message.args[0]


@pytest.mark.backend('TkAgg')
def test_show_gui_nowarning():
    plt.plot()
    with warnings.catch_warnings(record=True) as warns:
        warnings.simplefilter("always")
        plt.show(block=False)
        plt.close()
        assert len(warns) == 0

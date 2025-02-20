import pytest


from iss_tracker import data_range 
from iss_tracker import current_epoch
from iss_tracker import average_speed



#Last 2 data points in the the dataset

sample_xml_data = """                     

<ndm>
    <oem>
        <body>
            <segment>
                <data>
                    <stateVector>
                        <EPOCH>2025-063T11:58:30.000Z</EPOCH>
                        <X units="km">-2047.5298992042799</X>
                        <Y units="km">-4966.9397920931997</Y>
                        <Z units="km">4159.5637406105197</Z>
                        <X_DOT units="km/s">4.4275687047958101</X_DOT>
                        <Y_DOT units="km/s">-4.9897515611798999</Y_DOT>
                        <Z_DOT units="km/s">-3.7643525464400498</Z_DOT>
                    </stateVector>
                    <stateVector>
                        <EPOCH>2025-063T12:00:00.000Z</EPOCH>
                        <X units="km">-1639.2154505558599</X>
                        <Y units="km">-5389.7385494278196</Y>
                        <Z units="km">3799.9294936892502</Z>
                        <X_DOT units="km/s">4.6383139591721898</X_DOT>
                        <Y_DOT units="km/s">-4.3977167770952601</Y_DOT>
                        <Z_DOT units="km/s">-4.2206591026004903</Z_DOT>
                    </stateVector>
                </data>
            </segment>
        </body>
    </oem>
</ndm>

"""


def test_data_range(): 
    tests = data_range(sample_xml_data)

    assert "Data range is from 2025-03-04 11:58:30 to 2025-03-04 12:00:00"


def test_data_range_exceptions(): 
    with pytest.raises(AttributeError): 
        data_range(None)



def test_current_epoch(): 
    tests = current_epoch(sample_xml_data)

    assert "EPOCH:"
    assert "X:"
    assert "Y:"
    assert "Z:"
    assert "X_DOT:"
    assert "Y_DOT"
    assert "Z_DOT"


def test_current_epoch_excpetions(): 
    with pytest.raises(TypeError): 
        current_epoch(None)


def test_average_speed(): 
    tests = average_speed(sample_xml_data)

    assert "Average speed for the dataset: " 
    assert "Instatantaneous Speed:"


def test_average_speed_exceptions(): 
    with pytest.raises(TypeError): 
        average_speed(None)

import pytest
from survey import AnonymousSurvey as Survey

@pytest.fixture
def encuesta_prueba() -> Survey:
    question = "what language did you first learn to speak?"
    test_survey = Survey(question)
    return test_survey

def test_store_single_response(encuesta_prueba):
    encuesta_prueba.store_response("English")
    assert "English" in encuesta_prueba.responses

def test_store_three_responses(encuesta_prueba):
    responses = ["English", "Spanish", "Portuguese"]
    for response in responses:
        encuesta_prueba.store_response(response)

    for response in responses:
        assert response in encuesta_prueba.responses
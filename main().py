all_diseases = {
    "illness 1": {"symptom a", "symptom b", "symptom c"},
    "illness 2": {"symptom a", "symptom c", "symptom d", "symptom e", "symptom f"},
    "illness 3": {"symptom b", "symptom f", "symptom g"},
    "illness 4": {"symptom a", "symptom b", "symptom g"},
}

experienced_symptoms = {"symptom b", "symptom f"}



def get_disease_scores(
    symptoms: set[str], diseases: dict[str, set[str]]) -> dict[str, float]:
    scores = {}

    # Iterate over all diseases with their symptoms
    for disease, disease_symptoms in diseases.items():
        # Get the symptoms common to the disease and experienced ones
        common_symptoms = symptoms.intersection(disease_symptoms)
        # Calculate and keep track of score
        scores[disease] = len(common_symptoms) / len(disease_symptoms)

    return scores



print(get_disease_scores(experienced_symptoms, all_diseases))

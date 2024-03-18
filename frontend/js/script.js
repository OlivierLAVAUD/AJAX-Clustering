const modelInput = document.querySelector('.model-select');
const performanceScoreDisplay = document.getElementById('performance-score');

modelInput.addEventListener('change', async function() {
    const selectedModel = modelInput.value;
    console.log('Selected model:', selectedModel);

    async function score(selectedModel) {

        const apiUrl = `http://127.0.0.1:8000/evaluate_clustering_${selectedModel}/`;
        console.log(apiUrl)

        try {
            // Envoi de la requête à l'API avec le modèle sélectionné
            const response = await fetch(apiUrl, {
                method: 'GET',
            });

            // Vérification de la réponse HTTP
            if (response.ok) {
                // Récupération des données de réponse
                const data = await response.json();
                console.log('Performance score:', data["silhouette_score"]);

                // Afficher le score de performance dans la div
                performanceScoreDisplay.textContent = `Performance score for ${selectedModel}: ${data["silhouette_score"]}`;
            } else {
                console.error('Failed to fetch performance score from the API.');
                performanceScoreDisplay.textContent = 'Failed to fetch performance score';
            }
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }
    score(selectedModel)
});
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('transcribe-form');
  const transcriptEl = document.getElementById('transcript');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById('audio');
    const file = fileInput.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    transcriptEl.textContent = 'Transcribing...';
    transcriptEl.className = 'info';
    transcriptEl.classList.remove('hidden');

    try {
      const response = await fetch('/transcribe', {
        method: 'POST',
        body: formData
      });
      const result = await response.json();
      if (response.ok) {
        transcriptEl.textContent = result.transcript;
        transcriptEl.className = 'success';
      } else {
        transcriptEl.textContent = result.detail || 'Error during transcription';
        transcriptEl.className = 'error';
      }
    } catch (err) {
      transcriptEl.textContent = 'Failed to transcribe';
      transcriptEl.className = 'error';
    }
  });
});

const stars = document.querySelectorAll('.star');

function updateRating(value) {
    stars.forEach((star) => {
        star.classList.remove('text-warning');
    });
    for (let i = 0; i < value; i++) {
        stars[i].classList.add('text-warning');
    }
    document.getElementById('ratingValue').value = value;
}

stars.forEach((star) => {
    star.addEventListener('mouseover', (e) => {
        const value = e.target.getAttribute('data-star-value');
        updateRating(value);
    });

    star.addEventListener('mouseout', () => {
        const ratingInput = document.getElementById('ratingValue');
        const currentValue = ratingInput.value;
        updateRating(currentValue);
    });

    star.addEventListener('click', (e) => {
        const value = e.target.getAttribute('data-star-value');
        document.getElementById('ratingValue').value = value;
    });
});
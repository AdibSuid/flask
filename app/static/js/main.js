function filterCategory(category) {
    document.querySelectorAll('.portfolio-item').forEach(item => {
        if (category === 'all' || item.dataset.category === category)
            item.style.display = 'block';
        else
            item.style.display = 'none';
    });
}

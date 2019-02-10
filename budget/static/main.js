// Self executing function
(function() {
    document.querySelector('#categoryInput').addEventListener('keydown', function(e){
        if (e.keyCode != 13) {
            return;
        }

        var categoryName = this.value
        this.value = ''
        addNewCategory(categoryName)
        updateCategoriesString()
    })

    function addNewCategory(name) {
        document.querySelector('#categoriesContainer').insertAdjacentHTML('beforeend',
        `<li class="category">
                <span class="name">${name}</span>
                <span onclick="removeCategory(this)" class="btnRemove bold">x</span>
        </li>`
        )
    }
})()


function fetchCategoryArray() {
    var categories = []

    document.querySelector('.category').forEach(function(e) {
        name = e.querySelector('.name').innerHTML
        if (name == '') return

        categories.push(name)
    })
    return categories
}

function updateCategoriesString() {
    categories = fetchCategoryArray()
    document.querySelector('input[name="categoriesString"]').value = categories.join(',')
}

function removeCategory() {
    e.parentElement.remove()
    updateCategoriesString()
}

const form = document.getElementById('questionnaire-form');
const dietSection = document.querySelector('.diet-section');
const dietList = document.getElementById('diet-list');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const name = form.elements['name'].value;
  const age = form.elements['age'].value;
  const height = form.elements['height'].value;
  const weight = form.elements['weight'].value;

  // Aquí es donde llamarías a la función que genera la dieta personalizada
  const diet = generateDiet(name, age, height, weight);

  // Muestra la sección de la dieta personalizada y agrega los elementos a la lista
  dietSection.style.display = 'block';
  dietList.innerHTML = '';
  diet.forEach((item) => {
    const li = document.createElement('li');
    li.textContent = `${item.quantity} gramos de ${item.food} para ${item.meal}`;
    dietList.appendChild(li);
  });
});

// Esta es solo una función de ejemplo que genera una dieta personalizada aleatoria
function generateDiet(name, age, height, weight) {
  const meals = ['desayuno', 'almuerzo', 'cena'];
  const foods = ['pollo', 'pescado', 'carne', 'verduras', 'frutas', 'arroz', 'fideos', 'pan', 'yogur', 'queso', 'huevos'];
  const diet = [];
  for (const meal of meals) {
    const foodIndex = Math.floor(Math.random() * foods.length);
    const food = foods[foodIndex];
    const quantity = Math.floor(Math.random() * 100 + 50); // entre 50 y 150 gramos
    diet.push({
      meal: meal,
      food: food,
      quantity: quantity
    });
  }
  return diet;
}

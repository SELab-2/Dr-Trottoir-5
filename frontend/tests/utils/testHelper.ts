
/**
 * Gaat het v-model van een input veld triggeren (omdat de gewone manier niet werkt, hebben
 * we deze functie gemaakt)
 */
export function triggerInput(input, model, activator) {
  const data = activator(input.element.value)
  model.setData(data)
}

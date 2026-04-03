describe('Aplicação', () => {

  it('Carrega página inicial', () => {
    cy.visit('http://localhost:5173/')
    cy.get('body').should('be.visible')
  })

  it('Mostra elementos da tela', () => {
    cy.visit('http://localhost:5173/')
    cy.wait(2000)

    // tenta encontrar algo que SEMPRE aparece
    cy.contains('Sistema')
  })

})
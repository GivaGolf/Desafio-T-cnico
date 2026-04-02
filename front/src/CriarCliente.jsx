import { useState } from "react"
import axios from "axios"

function CriarCliente({ token, atualizarLista }) {
  const [nome, setNome] = useState("")
  const [email, setEmail] = useState("")
  const [telefone, setTelefone] = useState("")

  const criarCliente = async (e) => {
    e.preventDefault()

    try {
      await axios.post(
        "http://127.0.0.1:8000/clientes",
        {
          nome,
          email,
          telefone
        },
        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      )

      alert("Cliente criado com sucesso!")

      // limpar campos
      setNome("")
      setEmail("")
      setTelefone("")

      // atualizar lista
      atualizarLista()

    } catch (error) {
      alert("Erro ao criar cliente")
    }
  }

  return (
    <form onSubmit={criarCliente}>
      <h2>Criar Cliente</h2>

      <input
        placeholder="Nome"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
      />

      <input
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <input
        placeholder="Telefone"
        value={telefone}
        onChange={(e) => setTelefone(e.target.value)}
      />

      <button type="submit">Salvar</button>
    </form>
  )
}

export default CriarCliente
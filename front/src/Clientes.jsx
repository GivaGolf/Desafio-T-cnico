import { useEffect, useState } from "react"
import axios from "axios"
import CriarCliente from "./CriarCliente"

function Clientes({ token }) {
  const [clientes, setClientes] = useState([])

  const buscarClientes = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/clientes", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    console.log("RESPOSTA:", response.data)

    if (response.data && response.data.data) {
      setClientes(response.data.data)
    } else {
      alert("Resposta inesperada do servidor")
    }

  } catch (error) {
    console.log("ERRO COMPLETO:", error)
    alert("Erro ao buscar clientes")
  }
}

  useEffect(() => {
    buscarClientes()
  }, [])

  const deletarCliente = async (id) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/clientes/${id}`, {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })

      buscarClientes()
    } catch (error) {
      alert("Erro ao deletar cliente")
    }
  }

  return (
    <div>
      <h2>Clientes</h2>

      <CriarCliente token={token} atualizarLista={buscarClientes} />

      {clientes.map((cliente) => (
        <div key={cliente.id}>
          <p><b>Nome:</b> {cliente.nome || "Sem nome"}</p>
          <p><b>Email:</b> {cliente.email}</p>
          <p><b>Telefone:</b> {cliente.telefone}</p>

          <button onClick={() => deletarCliente(cliente.id)}>
            Deletar
          </button>

          <hr />
        </div>
      ))}
    </div>
  )
}

export default Clientes
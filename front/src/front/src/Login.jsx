import { useState } from "react"
import axios from "axios"

function Login({ setToken }) {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  const fazerLogin = async (e) => {
    e.preventDefault()

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/auth/login",
        {
          email,
          password
        }
      )

      const token = response.data.access_token

      // salva no estado
      setToken(token)

      // salva no navegador
      localStorage.setItem("token", token)

      alert("Login realizado com sucesso!")

    } catch (error) {
      alert("Erro no login")
    }
  }

  return (
    <form onSubmit={fazerLogin}>
      <h2>Login</h2>

      <input
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <input
        type="password"
        placeholder="Senha"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button type="submit">Entrar</button>
    </form>
  )
}

export default Login
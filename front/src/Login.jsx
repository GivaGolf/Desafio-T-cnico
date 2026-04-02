import { useState } from "react"
import axios from "axios"

function Login({ setToken }) {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  const handleLogin = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/auth/login", {
        email,
        password
      })

      const token = response.data.data.access_token

      localStorage.setItem("token", token)
      setToken(token)

    } catch (error) {
      alert("Erro no login")
    }
  }

  return (
    <div>
      <h2>Login</h2>

      <input
        placeholder="Email"
        onChange={(e) => setEmail(e.target.value)}
      />

      <input
        type="password"
        placeholder="Senha"
        onChange={(e) => setPassword(e.target.value)}
      />

      <button onClick={handleLogin}>Entrar</button>
    </div>
  )
}

export default Login
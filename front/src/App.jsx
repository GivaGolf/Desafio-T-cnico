import { useState } from "react"
import Clientes from "./Clientes"
import Login from "./Login"

function App() {
  const [token, setToken] = useState(localStorage.getItem("token") || "")

  const logout = () => {
    localStorage.removeItem("token")
    setToken("")
  }

  return (
    <div>
      <h1>Sistema</h1>

      {!token ? (
        <Login setToken={setToken} />
      ) : (
        <>
          <button onClick={logout}>Sair</button>
          <Clientes token={token} />
        </>
      )}
    </div>
  )
}

export default App
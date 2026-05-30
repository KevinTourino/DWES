import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import '../../css/login.css';

const Login = () => {

  const [formName, setFormName] = useState("");
  const [formPassword, setFormPassword] = useState("");

  const navigate = useNavigate();

  const onChangeName = (e) => {
    setFormName(e.target.value);
  }

  const onChangePassword = (e) => {
    setFormPassword(e.target.value);
  }

  const handleSubmit = (e) => {
    e.preventDefault();

    const name = formName.trim();
    const password = formPassword.trim();

    if (name.length != 0 && password.length != 0){
      axios.post("http://127.0.0.1:8000/api/token/", {
        username: formName,
        password: formPassword
      })
      .then((response) => {
        sessionStorage.setItem("access", response.data.access);
        window.dispatchEvent(new Event('authChange'))

        setFormName("");
        setFormPassword("");

        navigate("/");
      })
      .catch((error) => {
        console.error(error);
        alert("Usuario o contraseña incorrectos");
      });
    }
    else {
      alert("Los campos no pueden estar vacíos");
    }
  }

  return (
    <div className="login-container">
        <form className="login-form" onSubmit={handleSubmit}>
            <div className="form-group">
                <label htmlFor="nombre">Nombre</label>
                <input id="nombre" name="nombre" type="text" className="input" onChange={onChangeName} value={formName} />
            </div>

            <div className="form-group">
                <label htmlFor="password">Contraseña</label>
                <input id="password" name="password" type="password" className="input" onChange={onChangePassword} value={formPassword} />
            </div>

            <button type="submit" className="btn">Continuar</button>
            <div class="register">
              <p>
                No tienes una cuenta?{' '}
                <span
                  onClick={() => navigate('/register')}
                >
                  Regístrate aquí
                </span>
              </p>
            </div>
        </form>
    </div>
  )
}

export default Login
import { useState } from "react"
import '../../css/register.css';
import { useNavigate } from "react-router-dom";
import axios from "axios";

const Register = () => {


    const [formName, setFormName] = useState("");
    const [formEmail, setFormEmail] = useState("");
    const [formPassword, setFormPassword] = useState("");
    const [formPassword2, setFormPassword2] = useState("");

    const [error, setError] = useState("");

    const navigate = useNavigate();

    const onChangeName = (e) => {
        setFormName(e.target.value);
    }

    const onChangeEmail = (e) => {
        setFormEmail(e.target.value);
    }

    const onChangePassword = (e) => {
        setFormPassword(e.target.value);
    }

    const onChangePassword2 = (e) => {
        setFormPassword2(e.target.value);
    }

    const handleSubmit = (e) => {
        e.preventDefault()

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (formName.trim() == "") {
            console.log("Nombre invalido");
            setError("Nombre inválido");
            return;
        }

        if (!emailRegex.test(formEmail) || formEmail.trim() == "") {
            console.log("Email inválido");
            setError("Email inválido");
            return;
        }

        if (formPassword !== formPassword2 || formPassword.trim() == "" || formPassword2.trim() == "") {
            console.log("Las contraseñas no coinciden");
            setError("Contraseña inválido");
            return;
        }

        setError("");
        
        axios.post("http://127.0.0.1:8000/register/",
            {
                username: formName,
                email: formEmail,
                password: formPassword
            },
            {
                headers: {
                    "Content-Type": "application/json"
                }
            }
            )
            .then((response) => {
                
                axios.post("http://127.0.0.1:8000/api/token/", {
                    username: formName,
                    password: formPassword
                })
                .then((response) => {
                    console.log("ACCESS TOKEN:", response.data.access);
                    console.log("REFRESH TOKEN:", response.data.refresh);
                    sessionStorage.setItem("access", response.data.access);
                    sessionStorage.setItem("refresh", response.data.refresh);

                    navigate("/");
                })
                .catch((error) => {
                    console.error(error);
                    alert("Usuario o contraseña incorrectos");
                });

                setFormName("");
                setFormEmail("");
                setFormPassword("");
                setFormPassword2("");
            })
            .catch((error) => {
                console.log(JSON.stringify(error.response?.data, null, 2));
                alert(error.response?.data?.error || "Error en el registro");
        });
    }

    return (
        <div className="register-container">
        <form className="register-form" onSubmit={handleSubmit}>
            <div className="form-group">
            <label htmlFor="nombre">Nombre</label>
            <input id="nombre" name="nombre" type="text" className="input" onChange={onChangeName} value={formName} />
            </div>

            <div className="form-group">
            <label htmlFor="email">E-mail</label>
            <input id="email" name="email" type="email" className="input" onChange={onChangeEmail} value={formEmail} />
            </div>

            <div className="form-group">
            <label htmlFor="password">Contraseña</label>
            <input id="password" name="password" type="password" className="input" onChange={onChangePassword} value={formPassword} />
            </div>

            <div className="form-group">
            <label htmlFor="repeatPassword">Repite la contraseña</label>
            <input id="repeatPassword" name="repeatPassword" type="password" className="input" onChange={onChangePassword2} value={formPassword2} />
            </div>

            <button type="submit" className="btn">
                Crear perfil
            </button>
            {error && (
                <p style={{ color: "red", alignSelf: "center"}}>
                    {error}
                </p>
            )}
            <div class="register">
                <p>
                    Ya tienes una cuenta?{' '}
                    <span
                    onClick={() => navigate('/login')}
                    >
                    Inicia sesión aquí
                    </span>
                </p>
            </div>
        </form>
        </div>
    )
}

export default Register
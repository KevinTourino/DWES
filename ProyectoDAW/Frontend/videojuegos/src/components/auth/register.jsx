const Register = () => {


  return (
    <div>
        <form className="login-form" onSubmit={handleSubmit}>
            <div className="form-group">
                <label htmlFor="nombre">Nombre</label>
                <input id="nombre" name="nombre" type="text" className="input" />
            </div>

            <div className="form-group">
                <label htmlFor="email">E-mail</label>
                <input id="email" name="email" type="email" className="input" />
            </div>

            <div className="form-group">
                <label htmlFor="password">Contraseña</label>
                <input id="password" name="password" type="password" className="input" />
            </div>

            <div className="form-group">
                <label htmlFor="repeatPassword">Repite la contraseña</label>
                <input id="repeatPassword" name="repeatPassword" type="password" className="input"/>
            </div>

            <button type="submit" className="btn">Crear perfil</button>
        </form>
    </div>
  )
}

export default Register
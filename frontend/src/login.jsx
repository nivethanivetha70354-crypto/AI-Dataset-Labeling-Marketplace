import { useState } from 'react'
import './Login.css'
import { loginUser } from './api'

function Login({ onLogin, onRegister }) {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [remember, setRemember] = useState(false)
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (!email.trim()) {
      setError('Please enter your email.')
      return
    }

    if (!password.trim()) {
      setError('Please enter your password.')
      return
    }

    setError('')
    setLoading(true)

    try {
      const data = await loginUser(
        email.trim(),
        password
      )

      onLogin(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="login-page">
      <div className="login-card">

        <div className="login-logo">
          AI
        </div>

        <h1>Welcome back</h1>

        <p className="login-subtitle">
          Log in to your LabelMarket account
        </p>

        <form onSubmit={handleSubmit}>

          <div className="form-group">
            <label>Email</label>

            <input
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              disabled={loading}
            />
          </div>

          <div className="form-group">
            <label>Password</label>

            <input
              type="password"
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              disabled={loading}
            />
          </div>

          <div className="login-options">
            <label className="remember">
              <input
                type="checkbox"
                checked={remember}
                onChange={(e) =>
                  setRemember(e.target.checked)
                }
                disabled={loading}
              />

              <span>Remember me</span>
            </label>

            <button
              type="button"
              className="forgot-button"
              onClick={() =>
                alert(
                  'Password reset feature coming soon.'
                )
              }
            >
              Forgot password?
            </button>
          </div>

          {error && (
            <div className="login-error">
              {error}
            </div>
          )}

          <button
            type="submit"
            className="login-submit"
            disabled={loading}
          >
            {loading ? 'Logging in...' : 'Log in'}
          </button>

        </form>

        <div className="divider">
          <span></span>
          <p>or</p>
          <span></span>
        </div>

        <button
          type="button"
          className="google-button"
          onClick={() =>
            alert('Google login will be connected later.')
          }
        >
          <span className="google-icon">G</span>
          Continue with Google
        </button>

        <p className="register-link">
          Don't have an account?{' '}

          <button
            type="button"
            onClick={onRegister}
          >
            Create an account
          </button>
        </p>

      </div>
    </div>
  )
}

export default Login
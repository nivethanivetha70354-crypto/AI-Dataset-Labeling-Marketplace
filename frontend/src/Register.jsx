import { useState } from 'react'
import './Register.css'

function Register({ onRegister, onLogin }) {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [role, setRole] = useState('labeler')
  const [error, setError] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()

    if (!name.trim()) {
      setError('Please enter your full name.')
      return
    }

    if (!email.trim()) {
      setError('Please enter your email.')
      return
    }

    if (!password.trim()) {
      setError('Please enter your password.')
      return
    }

    if (password.length < 6) {
      setError('Password must be at least 6 characters.')
      return
    }

    setError('')

    // Send selected role to App.jsx
    onRegister(role)
  }

  return (
    <div className="register-page">
      <div className="register-card">

        <div className="register-logo">
          AI
        </div>

        <h1>Create your account</h1>

        <p className="register-subtitle">
          Join the LabelMarket community
        </p>

        <form onSubmit={handleSubmit}>

          {/* Full Name */}
          <div className="form-group">
            <label>Full name</label>

            <input
              type="text"
              placeholder="Enter your full name"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>

          {/* Email */}
          <div className="form-group">
            <label>Email</label>

            <input
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>

          {/* Password */}
          <div className="form-group">
            <label>Password</label>

            <input
              type="password"
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>

          {/* Role */}
          <div className="form-group">
            <label>Choose your role</label>

            <div className="role-options">

              {/* Labeler */}
              <button
                type="button"
                className={`role-card ${
                  role === 'labeler' ? 'selected' : ''
                }`}
                onClick={() => setRole('labeler')}
              >
                <div className="role-icon">
                  👤
                </div>

                <h3>Labeler</h3>

                <p>
                  Complete labeling tasks and earn money.
                </p>
              </button>

              {/* Dataset Owner */}
              <button
                type="button"
                className={`role-card ${
                  role === 'owner' ? 'selected' : ''
                }`}
                onClick={() => setRole('owner')}
              >
                <div className="role-icon">
                  🏢
                </div>

                <h3>Dataset Owner</h3>

                <p>
                  Upload datasets and create labeling
                  projects.
                </p>
              </button>

            </div>
          </div>

          {/* Error */}
          {error && (
            <div className="form-error">
              {error}
            </div>
          )}

          {/* Create Account */}
          <button
            type="submit"
            className="register-button"
          >
            Create Account
          </button>

        </form>

        {/* Login */}
        <p className="login-link">
          Already have an account?{' '}
          <button
            type="button"
            onClick={onLogin}
          >
            Log in
          </button>
        </p>

      </div>
    </div>
  )
}

export default Register
import './Dashboard.css'

function OwnerDashboard() {
  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <div className="brand">
          <span className="brand-icon">AI</span>
          <span>LabelMarket</span>
        </div>

        <div className="user-area">
          <span>Dataset Owner</span>
          <div className="avatar">N</div>
        </div>
      </header>

      <main className="dashboard-main">
        <div className="dashboard-title">
          <div>
            <span className="section-label">OWNER DASHBOARD</span>
            <h1>Welcome back 👋</h1>
            <p>Manage your datasets and labeling projects.</p>
          </div>

          <button className="primary-btn">
            + New Project
          </button>
        </div>

        <div className="dashboard-stats">
          <div className="stat-card">
            <span>Active Projects</span>
            <strong>8</strong>
            <small>Currently running</small>
          </div>

          <div className="stat-card">
            <span>Total Tasks</span>
            <strong>24,680</strong>
            <small>Across all projects</small>
          </div>

          <div className="stat-card">
            <span>Completed</span>
            <strong>18,420</strong>
            <small>Tasks completed</small>
          </div>

          <div className="stat-card">
            <span>Quality Rate</span>
            <strong>98%</strong>
            <small>Average quality</small>
          </div>
        </div>

        <section className="dashboard-section">
          <div className="section-heading">
            <div>
              <span className="section-label">PROJECTS</span>
              <h2>My labeling projects</h2>
            </div>

            <button className="view-btn">
              View all →
            </button>
          </div>

          <div className="project-list">
            <div className="project-card">
              <div className="project-top">
                <div>
                  <span className="live-status">● LIVE</span>
                  <h3>Image Classification</h3>
                  <p>Product image dataset</p>
                </div>

                <strong>72%</strong>
              </div>

              <div className="progress">
                <div
                  className="progress-bar"
                  style={{ width: '72%' }}
                ></div>
              </div>

              <div className="project-bottom">
                <span>7,160 / 10,000 tasks</span>
                <span>$1,800 budget</span>
              </div>
            </div>

            <div className="project-card">
              <div className="project-top">
                <div>
                  <span className="live-status">● LIVE</span>
                  <h3>Customer Sentiment</h3>
                  <p>Text classification dataset</p>
                </div>

                <strong>45%</strong>
              </div>

              <div className="progress">
                <div
                  className="progress-bar"
                  style={{ width: '45%' }}
                ></div>
              </div>

              <div className="project-bottom">
                <span>4,500 / 10,000 tasks</span>
                <span>$1,200 budget</span>
              </div>
            </div>

            <div className="project-card">
              <div className="project-top">
                <div>
                  <span className="completed-status">
                    ● COMPLETED
                  </span>
                  <h3>Vehicle Detection</h3>
                  <p>Road image dataset</p>
                </div>

                <strong>100%</strong>
              </div>

              <div className="progress">
                <div
                  className="progress-bar"
                  style={{ width: '100%' }}
                ></div>
              </div>

              <div className="project-bottom">
                <span>8,000 / 8,000 tasks</span>
                <span>$2,400 budget</span>
              </div>
            </div>
          </div>
        </section>

        <section className="upload-section">
          <div>
            <span className="section-label">
              START A NEW PROJECT
            </span>

            <h2>Have a dataset ready?</h2>

            <p>
              Upload your dataset and connect with skilled
              labelers.
            </p>
          </div>

          <button className="primary-btn">
            Upload Dataset →
          </button>
        </section>
      </main>
    </div>
  )
}

export default OwnerDashboard
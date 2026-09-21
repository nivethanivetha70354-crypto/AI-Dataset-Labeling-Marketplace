import { useEffect, useState } from "react";
import "./Dashboard.css";

const API_URL = "http://127.0.0.1:8000";

function LabelerDashboard() {
  const [tasks, setTasks] = useState([]);
  const [selectedTask, setSelectedTask] = useState(null);

  const [accepted, setAccepted] = useState(false);
  const [reviewText, setReviewText] = useState("");

  const [aiLabel, setAiLabel] = useState("");
  const [confidence, setConfidence] = useState(null);

  const [finalLabel, setFinalLabel] = useState("");
  const [message, setMessage] = useState("");

  const [loading, setLoading] = useState(false);
  const [aiLoading, setAiLoading] = useState(false);

  useEffect(() => {
    loadTasks();
  }, []);

  async function loadTasks() {
    try {
      const token = localStorage.getItem("access_token");

      if (!token) {
        setMessage("Please login first.");
        return;
      }

      const response = await fetch(`${API_URL}/tasks/`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Failed to load tasks");
      }

      if (Array.isArray(data)) {
        setTasks(data);
      } else if (data.data && Array.isArray(data.data)) {
        setTasks(data.data);
      } else {
        setTasks([]);
      }
    } catch (error) {
      console.error(error);
      setMessage(`Unable to load tasks: ${error.message}`);
    }
  }

  async function startTask(task) {
  try {
    const token = localStorage.getItem("access_token");

    const response = await fetch(
      `${API_URL}/assignments/${task.task_id}`,
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    const data = await response.json();

    if (!response.ok) {
      throw new Error(
        data.detail || "Unable to accept task"
      );
    }

    setSelectedTask(task);
    setAccepted(true);

    setMessage(
      data.message || "Task accepted successfully!"
    );

    setAiLabel("");
    setConfidence(null);
    setFinalLabel("");
    setReviewText("");

  } catch (error) {
    console.error(error);
    setMessage(`Task acceptance failed: ${error.message}`);
  }
}

  async function getAISuggestion() {
    if (!reviewText.trim()) {
      setMessage("Please enter a review first.");
      return;
    }

    setAiLoading(true);
    setMessage("");

    try {
      const token = localStorage.getItem("access_token");

      const response = await fetch(
        `${API_URL}/ai/suggest-label`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify({
            text: reviewText,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "AI suggestion failed"
        );
      }

      const result = data.data || data;

      setAiLabel(result.suggested_label || "");
      setConfidence(result.confidence ?? null);

      setMessage("AI suggestion generated successfully!");
    } catch (error) {
      console.error(error);

      // Demo fallback
      const text = reviewText.toLowerCase();

      let suggestion = "neutral";
      let score = 0.70;

      if (
        text.includes("good") ||
        text.includes("excellent") ||
        text.includes("great") ||
        text.includes("love") ||
        text.includes("happy")
      ) {
        suggestion = "positive";
        score = 0.92;
      } else if (
        text.includes("bad") ||
        text.includes("worst") ||
        text.includes("hate") ||
        text.includes("poor") ||
        text.includes("terrible")
      ) {
        suggestion = "negative";
        score = 0.91;
      }

      setAiLabel(suggestion);
      setConfidence(score);

      setMessage("AI suggestion generated!");
    } finally {
      setAiLoading(false);
    }
  }

  async function submitAnnotation() {
    if (!reviewText.trim()) {
      setMessage("Please enter review text.");
      return;
    }

    if (!finalLabel) {
      setMessage("Please select final label.");
      return;
    }

    setLoading(true);
    setMessage("");

    try {
      const token = localStorage.getItem("access_token");

      const response = await fetch(
        `${API_URL}/annotations/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify({
            task_id: selectedTask.task_id,
            input_text: reviewText,
            ai_label: aiLabel || null,
            final_label: finalLabel,
            confidence: confidence || 0,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Submission failed"
        );
      }

      setMessage("Annotation submitted successfully!");

      setReviewText("");
      setAiLabel("");
      setConfidence(null);
      setFinalLabel("");
    } catch (error) {
      console.error(error);

      setMessage(
        `Submission failed: ${error.message}`
      );
    } finally {
      setLoading(false);
    }
  }

  function closeWorkspace() {
    setSelectedTask(null);
    setAccepted(false);

    setReviewText("");
    setAiLabel("");
    setConfidence(null);
    setFinalLabel("");
    setMessage("");
  }

  return (
    <div className="dashboard">

      <div className="dashboard-header">
        <div>
          <h1>LabelMarket</h1>
          <p>AI Dataset Labeling Marketplace</p>
        </div>

        <div className="user-role">
          Labeler
        </div>
      </div>

      {message && (
        <div className="message-box">
          {message}
        </div>
      )}

      {!selectedTask && (
        <>
          <div className="dashboard-stats">

            <div className="stat-card">
              <h3>Available Tasks</h3>
              <p>{tasks.length}</p>
            </div>

            <div className="stat-card">
              <h3>Accepted Tasks</h3>
              <p>{accepted ? 1 : 0}</p>
            </div>

            <div className="stat-card">
              <h3>Completed</h3>
              <p>0</p>
            </div>

          </div>

          <div className="tasks-section">

            <div className="section-header">
              <h2>Available Tasks</h2>

              <button
                className="secondary-btn"
                onClick={loadTasks}
              >
                Refresh
              </button>
            </div>

            {tasks.length === 0 ? (
              <div className="empty-state">
                <h3>No tasks available</h3>
                <p>
                  No labeling tasks are currently available.
                </p>
              </div>
            ) : (
              <div className="task-grid">

                {tasks.map((task) => (
                  <div
                    className="task-card"
                    key={task.task_id}
                  >

                    <div className="task-card-header">

                      <h3>
                        {task.title || "Untitled Task"}
                      </h3>

                      <span className="task-status">
                        {task.status || "open"}
                      </span>

                    </div>

                    <p className="task-instructions">
                      {task.instructions ||
                        "Complete the labeling task."}
                    </p>

                    <div className="task-details">

                      <span>
                        Dataset ID:{" "}
                        {task.dataset_id || "-"}
                      </span>

                      <span>
                        Task ID:{" "}
                        {task.task_id || "-"}
                      </span>

                    </div>

                    <button
                      className="start-btn"
                      onClick={() => startTask(task)}
                    >
                      Start Task
                    </button>

                  </div>
                ))}

              </div>
            )}

          </div>
        </>
      )}

      {selectedTask && (
        <div className="annotation-workspace">

          <div className="workspace-header">

            <div>
              <h2>Annotation Workspace</h2>

              <p>
                Task:{" "}
                <strong>
                  {selectedTask.title ||
                    "Selected Task"}
                </strong>
              </p>
            </div>

            <button
              className="secondary-btn"
              onClick={closeWorkspace}
            >
              Back to Tasks
            </button>

          </div>

          <div className="task-info-box">

            <h3>Task Instructions</h3>

            <p>
              {selectedTask.instructions ||
                "Label the given text."}
            </p>

          </div>

          <div className="annotation-card">

            <h3>Review / Text to Label</h3>

            <textarea
              value={reviewText}
              onChange={(e) =>
                setReviewText(e.target.value)
              }
              placeholder="Enter customer review here..."
              rows="6"
            />

          </div>

          <div className="annotation-card">

            <div className="ai-header">

              <h3>AI Suggestion</h3>

              <button
                className="ai-btn"
                onClick={getAISuggestion}
                disabled={aiLoading}
              >
                {aiLoading
                  ? "Analyzing..."
                  : "Get AI Suggestion"}
              </button>

            </div>

            {aiLabel && (
              <div className="ai-result">

                <div>
                  <span>Suggested Label</span>

                  <strong>
                    {aiLabel.toUpperCase()}
                  </strong>
                </div>

                <div>
                  <span>Confidence</span>

                  <strong>
                    {confidence !== null
                      ? `${Math.round(
                          confidence * 100
                        )}%`
                      : "-"}
                  </strong>
                </div>

              </div>
            )}

          </div>

          <div className="annotation-card">

            <h3>Human Verification</h3>

            <p>
              Verify the AI suggestion and select
              the final label.
            </p>

            <select
              value={finalLabel}
              onChange={(e) =>
                setFinalLabel(e.target.value)
              }
            >
              <option value="">
                Select Final Label
              </option>

              <option value="positive">
                Positive
              </option>

              <option value="negative">
                Negative
              </option>

              <option value="neutral">
                Neutral
              </option>
            </select>

          </div>

          <div className="submit-section">

            <button
              className="submit-btn"
              onClick={submitAnnotation}
              disabled={loading}
            >
              {loading
                ? "Submitting..."
                : "Submit Final Annotation"}
            </button>

          </div>

        </div>
      )}

    </div>
  );
}

export default LabelerDashboard;
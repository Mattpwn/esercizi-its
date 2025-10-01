import  { useState } from "react";

const TodoItem = ({ task, onDeleteTask, onToggleTask }) => {
  const [isEditing, setIsEditing] = useState(false);
  return (
    <li className="list-group-item d-flex justify-content-between">
      <div>
        {isEditing ? (
          <input type="text"></input>
        ) : (
          <>
            <input
              type="checkbox"
              checked={task.completed}
              className="form-check-input me-2"
              onChange={() => {
                onToggleTask(task.id, task.completed);
              }}
            ></input>
            <span
              style={{
                textDecoration: task.completed ? "line-through" : "none",
              }}
            >
              {task.text}
            </span>
          </>
        )}
      </div>
      <button
        className="btn btn-danger"
        onClick={() => {
          onDeleteTask(task.id);
        }}
      >
        Delete
      </button>
    </li>
  );
};

export default TodoItem;

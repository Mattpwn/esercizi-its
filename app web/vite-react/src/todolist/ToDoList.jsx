import ToDoItem from './ToDoItem'

const ToDoList = ({ tasks, onDeleteTask,onToggleTask }) => {
    return (
      <ul className="list-group">
        {tasks.map((t) => {
          return (
            <ToDoItem key={t.id} task={t} onDeleteTask={onDeleteTask} onToggleTask={onToggleTask}></ToDoItem>
          );
        })}
      </ul>
    );
  };
  
  export default ToDoList;
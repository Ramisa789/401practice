import { useState } from "react";

const UpdateTeacher = () => {
    const [teacherId, setTeacherId] = useState("");
    const [name, setName] = useState("");
    const [age, setAge] = useState("");
    const [message, setMessage] = useState("");

    const handleUpdate = async () => {
        const response = await fetch(`http://127.0.0.1:8000/teachers/${teacherId}/`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ name, age }),
        });

        const data = await response.json();

        if (response.ok) {
            setMessage("Teacher updated successfully!");
        } else {
            setMessage(data.error || "Failed to update teacher.");
        }
    };

    return (
        <div style={{ padding: "20px" }}>
            <h2>Update Teacher</h2>
            <input
                type="number"
                placeholder="Teacher ID"
                value={teacherId}
                onChange={(e) => setTeacherId(e.target.value)}
            />
            <input
                type="text"
                placeholder="New Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />
            <input
                type="number"
                placeholder="New Age"
                value={age}
                onChange={(e) => setAge(e.target.value)}
            />
            <button onClick={handleUpdate}>Update</button>
            <p>{message}</p>
        </div>
    );
};

export default UpdateTeacher;

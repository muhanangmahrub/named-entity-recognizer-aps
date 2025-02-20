import React from "react";

export default function TextField() {
  return (
    <div>
      <label style={{ padding: "10px" }}>
        Enter your text:
        <br />
        <textarea
          name="postText"
          defaultValue="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
          rows={4}
          cols={40}
          style={{
            padding: "10px",
            border: "solid",
            height: "20rem",
            width: "50rem",
          }}
        />
      </label>
      <br />
      <button style={{ backgroundColor: "#04AA6D", color: "white" }}>
        Process
      </button>
    </div>
  );
}

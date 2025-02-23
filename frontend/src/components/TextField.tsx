interface Props {
  onTextChange: (text: string) => void;
}

const TextField = ({ onTextChange }: Props) => {
  return (
    <fieldset
      style={{
        width: "100vw",
        // border: "1px solid black",
        padding: "10px",
        borderRadius: "6px",
      }}
    >
      <legend style={{ fontWeight: "bold", marginBottom: "8px" }}>
        Enter your text:
      </legend>
      <textarea
        placeholder="Type your text here..."
        style={{
          width: "100%",
          padding: "8px",
          fontSize: "16px",
          borderRadius: "4px",
          border: "1px solid black",
        }}
        onChange={(e) => onTextChange(e.target.value)}
      />
    </fieldset>
  );
};

export default TextField;

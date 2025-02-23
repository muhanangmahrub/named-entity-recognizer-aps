interface Props {
  model: string;
  setModel: (model: string) => void;
}

const ModelSelector = ({ model, setModel }: Props) => {
  return (
    <div style={{ marginBottom: "10px" }}>
      <label
        style={{ display: "block", fontWeight: "bold", marginBottom: "8px" }}
      >
        Model
      </label>
      <select
        value={model}
        onChange={(e) => setModel(e.target.value)}
        style={{
          padding: "8px",
          border: "1px solid black",
          borderRadius: "4px",
          cursor: "pointer",
        }}
      >
        <option value="spacy">spaCy</option>
        <option value="crfs">CRF</option>
        <option value="bert">BERT</option>
      </select>
    </div>
  );
};

export default ModelSelector;

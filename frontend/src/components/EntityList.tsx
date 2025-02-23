interface Props {
  entities: Record<string, string>;
}

const EntityList = ({ entities }: Props) => {
  return (
    <div
      style={{
        width: "100vw",
        marginTop: "24px",
        padding: "10px",
        borderRadius: "6px",
      }}
    >
      <h3 style={{ fontWeight: "bold", marginBottom: "8px" }}>Entities</h3>
      <ul style={{ listStyleType: "none", padding: 0 }}>
        {Object.entries(entities).map(([word, entity]) => (
          <li key={word} style={{ marginBottom: "4px" }}>
            <strong>{word}</strong>: {entity}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EntityList;

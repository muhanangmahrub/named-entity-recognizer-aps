import { ChakraProvider, Button } from "@chakra-ui/react";
import { defaultSystem } from "@chakra-ui/react";
import Header from "./components/Header";
import TextField from "./components/TextField";
import { useState } from "react";
import ModelSelector from "./components/ModelSelector";
import EntityList from "./components/EntityList";

function App() {
  const [text, setText] = useState<string>("");
  const [model, setModel] = useState<string>("spacy");
  const [entities, setEntities] = useState<Record<string, string>>({});

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, model }),
    });

    const data = await response.json();
    setEntities(data);
  };

  return (
    <ChakraProvider value={defaultSystem}>
      <Header />
      <form
        onSubmit={handleSubmit}
        style={{
          width: "100vw",
          height: "100vh",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          padding: "20px",
          boxSizing: "border-box",
        }}
      >
        <ModelSelector model={model} setModel={setModel} />
        <TextField onTextChange={setText} />
        <Button type="submit">Process</Button>
        <EntityList entities={entities} />
      </form>
    </ChakraProvider>
  );
}

export default App;

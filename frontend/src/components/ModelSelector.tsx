import { Box, Text } from "@chakra-ui/react";

interface Props {
  model: string;
  setModel: (model: string) => void;
}

const ModelSelector = ({ model, setModel }: Props) => {
  return (
    <Box>
      <Text>Model</Text>
      <select
        value={model}
        onChange={(e) => setModel(e.target.value)}
        style={{ border: "black" }}
      >
        <option value="spacy">spaCy</option>
        <option value="crfs">CRF</option>
        <option value="bert">BERT</option>
      </select>
    </Box>
  );
};

export default ModelSelector;

import { Box, Heading } from "@chakra-ui/react";

const Header = () => {
  return (
    <Box
      as="header"
      position="fixed"
      top={0}
      width="100%"
      bg="gray.100"
      py={4}
      px={6}
      boxShadow="md"
      zIndex={1000}
    >
      <Heading size="lg">Named Entity App</Heading>
    </Box>
  );
};

export default Header;

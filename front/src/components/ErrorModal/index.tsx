import React from "react";
import Box from "@mui/material/Box";
import Modal from "@mui/material/Modal";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";

const style = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: 400,
  bgcolor: "background.paper",
  boxShadow: 24,
  p: 4,
};

type Props = {
  isErrorModalOpen: boolean;
  setIsErrorModalOpen: React.Dispatch<React.SetStateAction<boolean>>;
};

const ErrorModal: React.FC<Props> = ({
  isErrorModalOpen,
  setIsErrorModalOpen,
}) => {
  return (
    <Modal
      open={isErrorModalOpen}
      onClose={() => setIsErrorModalOpen(false)}
      aria-labelledby="error-modal-title"
      aria-describedby="error-modal-description"
    >
      <Box sx={style}>
        <Typography id="error-modal-title" variant="h6" component="h2">
          Something Went Wrong
        </Typography>
        <Typography sx={{ mt: 2 }}>Try to enter another data</Typography>
        <Box sx={{ textAlign: "right", mt: 2 }}>
          <Button
            variant="contained"
            onClick={() => setIsErrorModalOpen(false)}
          >
            Close
          </Button>
        </Box>
      </Box>
    </Modal>
  );
};

export default ErrorModal;

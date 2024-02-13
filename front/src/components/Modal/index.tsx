import { Button, Modal, Typography, Box, TextField } from "@mui/material";

const modalStyle = {
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
  modalOpen: boolean;
  handleClose: () => void;
  handleChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  formData: {
    name: string;
    longitude: string;
    latitude: string;
    first_street: string;
    second_street: string;
  };
  handleModalSubmit: () => void;
};

const MainModal: React.FC<Props> = ({
  modalOpen,
  handleClose,
  handleChange,
  formData,
  handleModalSubmit,
}) => {
  const isFormValid =
    formData.name &&
    formData.longitude &&
    formData.latitude &&
    formData.first_street &&
    formData.second_street;

  return (
    <Modal open={modalOpen} onClose={handleClose}>
      <Box sx={modalStyle}>
        <Typography id="add-intersection-modal" variant="h6" component="h2">
          Add Intersection
        </Typography>
        <Box
          component="form"
          sx={{ "& .MuiTextField-root": { mt: 2 } }}
          noValidate
          autoComplete="off"
        >
          <TextField
            fullWidth
            required
            id="name"
            name="name"
            label="Intersection Name"
            value={formData.name}
            onChange={handleChange}
          />
          <TextField
            fullWidth
            required
            type="number"
            id="longitude"
            name="longitude"
            label="Longitude (format xx.xxxxx)"
            value={formData.longitude}
            onChange={handleChange}
          />
          <TextField
            fullWidth
            required
            type="number"
            id="latitude"
            name="latitude"
            label="Latitude (format xx.xxxxx)"
            value={formData.latitude}
            onChange={handleChange}
          />
          <TextField
            fullWidth
            required
            id="first_street"
            name="first_street"
            label="First Street"
            value={formData.first_street}
            onChange={handleChange}
          />
          <TextField
            fullWidth
            required
            id="second_street"
            name="second_street"
            label="Second Street"
            value={formData.second_street}
            onChange={handleChange}
          />
          <Box sx={{ display: "flex", justifyContent: "space-between", mt: 2 }}>
            <Button onClick={handleClose} sx={{ mr: 1 }}>
              Cancel
            </Button>
            <Button
              variant="contained"
              disabled={!isFormValid}
              onClick={() => handleModalSubmit()}
            >
              Submit
            </Button>
          </Box>
        </Box>
      </Box>
    </Modal>
  );
};
export default MainModal;

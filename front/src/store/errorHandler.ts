import { StoreApi } from "zustand";
import { IntersectionStore } from "./types";
import { AxiosError } from "axios";

export const handleAxiosError = (
  error: AxiosError,
  set: StoreApi<IntersectionStore>["setState"],
) => {
  if (error.response || error.request) {
    set({ error: { message: error.message } });
  }
};

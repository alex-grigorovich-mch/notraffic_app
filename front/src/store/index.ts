import { create } from "zustand";
import { IntersectionStore } from "./types";
import axios from "axios";
import { handleAxiosError } from "./errorHandler";


const useIntersectionsStore = create<IntersectionStore>(set => ({
  intersections: [],
  error: null,

  addIntersection: async (
    name,
    longitude,
    latitude,
    first_street,
    second_street,
  ) => {
    try {
      const newIntersection = {
        name,
        longitude,
        latitude,
        first_street,
        second_street,
      };
      const response = await axios.post(
        "http://0.0.0.0:8000/api/v1/notraffic/",
        newIntersection,
      );
      set(state => ({
        intersections: [...state.intersections, response.data],
      }));
    } catch (error) {
      console.error("Failed to remove intersection:", error);
      if (axios.isAxiosError(error)) handleAxiosError(error, set);
    }
  },

  removeIntersection: async id => {
    try {
      await axios.delete(`http://0.0.0.0:8000/api/v1/notraffic/${id}`);
      set(state => ({
        intersections: state.intersections.filter(
          intersection => intersection.id !== id,
        ),
      }));
    } catch (error) {
      console.error("Failed to remove intersection:", error);
      if (axios.isAxiosError(error)) handleAxiosError(error, set);
    }
  },

  updateIntersection: async (
    id,
    name,
    longitude,
    latitude,
    first_street,
    second_street,
  ) => {
    try {
      const updatedIntersection = {
        name,
        longitude,
        latitude,
        first_street,
        second_street,
      };
      await axios.put(
        `http://0.0.0.0:8000/api/v1/notraffic/${id}/`,
        updatedIntersection,
      );
      set(state => ({
        intersections: state.intersections.map(intersection =>
          intersection.id === id
            ? { ...intersection, ...updatedIntersection }
            : intersection,
        ),
      }));
    } catch (error) {
      console.error("Failed to remove intersection:", error);
      if (axios.isAxiosError(error)) handleAxiosError(error, set);
    }
  },

  fetchIntersections: async () => {
    try {
      const response = await axios.get("http://0.0.0.0:8000/api/v1/notraffic/");
      set({ intersections: response.data });
    } catch (error) {
      console.error("Failed to remove intersection:", error);
      if (axios.isAxiosError(error)) handleAxiosError(error, set);
    }
  },
}));

export default useIntersectionsStore;

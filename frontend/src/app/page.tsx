"use client";
import { useState } from "react";

export default function Home() {
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="w-full max-w-md bg-white rounded-2xl shadow-lg p-6 space-y-6">
        <h2 className="text-2xl font-bold text-center text-gray-800">Add Product</h2>

        <form
          onSubmit={(e) => {
            e.preventDefault();
            const formData = new FormData(e.target as HTMLFormElement);
            const data = Object.fromEntries(formData.entries());

            fetch("http://127.0.0.1:8000/product", {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify(data),
            })
              .then((response) => {
                if (!response.ok) {
                  throw new Error("Failed to submit data");
                }
                return response.json();
              })
              .then((result) => {
                setResponse(result);
                setError(null);
              })
              .catch((err) => {
                setError(err.message);
                setResponse(null);
              });
          }}
          className="space-y-4"
        >
          <div>
            <label htmlFor="name" className="block text-sm font-medium text-gray-700">
              Name
            </label>
            <input
              type="text"
              id="name"
              name="name"
              required
              className="mt-1 block w-full px-4 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
            />
          </div>

          <div>
            <label htmlFor="price" className="block text-sm font-medium text-gray-700">
              Price
            </label>
            <input
              type="number"
              id="price"
              name="price"
              required
              className="mt-1 block w-full px-4 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
            />
          </div>

          <div>
            <label htmlFor="description" className="block text-sm font-medium text-gray-700">
              Description
            </label>
            <textarea
              id="description"
              name="description"
              required
              className="mt-1 block w-full px-4 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
            ></textarea>
          </div>

          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 rounded-lg font-semibold hover:bg-blue-600 transition"
          >
            Submit
          </button>
        </form>

        {response && (
          <div className="bg-green-100 text-green-800 px-4 py-3 rounded-md">
            <strong>Success:</strong> {JSON.stringify(response)}
          </div>
        )}

        {error && (
          <div className="bg-red-100 text-red-800 px-4 py-3 rounded-md">
            <strong>Error:</strong> {error}
          </div>
        )}
      </div>
    </div>
  );
}

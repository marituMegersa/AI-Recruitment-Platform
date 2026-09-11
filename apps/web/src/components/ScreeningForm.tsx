import React, { useState } from 'react';

export function ScreeningForm({ onSubmit }: { onSubmit: (data: any) => void }) {
  const [name, setName] = useState('Abebe Bikila');
  const [email, setEmail] = useState('abebe@example.com');
  const [skills, setSkills] = useState('Python, FastAPI, React, PyTorch, Docker');
  const [exp, setExp] = useState(4.5);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit({
      candidate_name: name,
      candidate_email: email,
      skills: skills.split(',').map(s => s.trim()),
      experience_years: Number(exp)
    });
  };

  return (
    <form onSubmit={handleSubmit} style={{ background: '#fff', padding: '1.5rem', borderRadius: '8px', border: '1px solid #e2e8f0', marginBottom: '1.5rem' }}>
      <h3 style={{ margin: '0 0 1rem 0', color: '#0f172a' }}>📄 Candidate Screening Intake</h3>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Candidate Name</label>
          <input value={name} onChange={e => setName(e.target.value)} required style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Email Address</label>
          <input type="email" value={email} onChange={e => setEmail(e.target.value)} required style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Years of Experience</label>
          <input type="number" step="0.5" value={exp} onChange={e => setExp(Number(e.target.value))} required style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Skills (Comma-separated)</label>
          <input value={skills} onChange={e => setSkills(e.target.value)} required style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
      </div>
      <button type="submit" style={{ marginTop: '1rem', background: '#0d9488', color: '#fff', padding: '0.75rem 1.5rem', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}>
        Screen & Match Candidate
      </button>
    </form>
  );
}
